use actix_web::web::Data;
use actix_web::{get, post, web, HttpResponse, Responder};
use reqwest;
use serde::Deserialize;
use serde_json::Value;
use tera::{Context, Tera};

#[get("/")]
pub async fn index(templates: Data<Tera>) -> impl Responder {
    let mut ctx = Context::new();
    ctx.insert("emo_result", &"null");
    let view = templates.render("index.html", &ctx);

    match view {
        Ok(body) => HttpResponse::Ok().body(body),
        Err(e) => HttpResponse::InternalServerError().body(e.to_string()),
    }
}

#[derive(Deserialize)]
pub struct FormText {
    text: String,
}

#[post("/")]
pub async fn get_album(
    web::Form(form): web::Form<FormText>,
    templates: Data<Tera>,
) -> impl Responder {
    let json_1 = "{\"query\":\"mutation{declareRequestBody(text:".to_string();
    let text = format!("\\\"{}\\\"", &form.text);
    let json_2 = ")}\"}".to_string();

    let json_string = json_1 + &text + &json_2;

    let json_item = serde_json::from_str(&json_string).unwrap();

    let res = send_post_to_bff(json_item);
    match res.await {
        Ok(res) => {
            let graphql_json: _ = serde_json::from_str::<Value>(&res).unwrap();
            let tmp = graphql_json["data"]
                .as_object()
                .unwrap()
                .get("declareRequestBody")
                .unwrap()
                .to_string();
            let res_json = serde_json::from_str(&tmp).unwrap();

            let ctx = Context::from_value(res_json);
            match ctx {
                Ok(ctx) => {
                    let view = templates.render("index.html", &ctx);
                    match view {
                        Ok(body) => HttpResponse::Ok().content_type("text/html").body(body),
                        Err(e) => HttpResponse::InternalServerError().body(e.to_string()),
                    }
                }
                Err(e) => HttpResponse::InternalServerError().body(e.to_string()),
            }
        }
        Err(e) => HttpResponse::InternalServerError().body(e.to_string()),
    }
}

pub async fn send_post_to_bff(json: serde_json::Value) -> reqwest::Result<String> {
    let client = reqwest::Client::new();
    let responce = client
        .post("http://bff:9000/graphql")
        .json(&json)
        .send()
        .await?;
    responce.text().await
}
