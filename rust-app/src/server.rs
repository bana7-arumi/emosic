use actix_web::{get, post, web, HttpResponse, Responder};
use reqwest;
use serde_json;
use tera::Tera;
#[get("/")]
pub async fn hello(templates: web::Data<Tera>) -> impl Responder {
    let view = templates.render("index.html", &tera::Context::new());

    match view {
        Ok(body) => HttpResponse::Ok().content_type("text/html").body(body),
        Err(e) => HttpResponse::InternalServerError().body(e.to_string()),
    }
}
#[post("/post")]
pub async fn post_example(item: web::Json<serde_json::Value>) -> impl Responder {
    format!("responce is \n",);
    let res = send_post_to_bff(item.0);
    match res.await {
        Ok(res) => HttpResponse::Ok().content_type("text/html").body(res),
        Err(e) => HttpResponse::InternalServerError().body(e.to_string()),
    }
}

pub async fn send_post_to_bff(json: serde_json::Value) -> reqwest::Result<String> {
    let client = reqwest::Client::new();
    let responce = client
        .post("http://bff:9000/post")
        .json(&json) //ひどい実装ですみませんが動作確認なので許してほしいです
        .send()
        .await?;
    responce.text().await
}
