use actix_web::{get, post, web, HttpResponse, Responder, body};
use reqwest;
use serde::Deserialize;
use serde_json::{self, Map};
use tera::Tera;
use tera::Context;

#[get("/")]
pub async fn hello(templates: web::Data<Tera>) -> impl Responder {
    let view = templates.render("index.html", &tera::Context::new());

    match view {
        Ok(body) => HttpResponse::Ok().content_type("text/html").body(body),
        Err(e) => HttpResponse::InternalServerError().body(e.to_string()),
    }
}

#[derive(Deserialize)]
struct FormText {
    text: String,
}

// #[derive(Deserialize)]
// struct Image {
//     url: String,
//     height: String,
//     weight: String
// }

// #[derive(Deserialize)]
// struct Response {
//     emo_result: String,
//     name: String,
//     uri: String,
//     image: Image
// }

#[post("/")]
pub async fn post_example(web::Form(form): web::Form<FormText>, templates: web::Data<Tera>) -> impl Responder {
    let json_string = format!("{{\"text\":\"{}\"}}", form.text);
    let json_item = serde_json::from_str(&json_string).unwrap();

    let res = send_post_to_bff(json_item);
    match res.await {
        Ok(res) => {
            let res_json = serde_json::from_str(&res).unwrap();
            let ctx = Context::from_value(res_json);
            match ctx {
                Ok(ctx) => {
                    let view = templates.render("index.html", &ctx);
                    match view {
                        Ok(body) => HttpResponse::Ok().content_type("text/html").body(body),
                        Err(e) => HttpResponse::InternalServerError().body(e.to_string()),
                    }
                },
                Err(e) => HttpResponse::InternalServerError().body(e.to_string()),
            }
        },
        Err(e) => HttpResponse::InternalServerError().body(e.to_string()),
    }

    // let res = send_post_to_bff(json_item);

    // // match res.await {
    // //     Ok(res) => render_html(res, templates),
    // //     Err(e) => HttpResponse::InternalServerError().body(e.to_string()),
    // // }

    // let res_json = match res.await {
    //     Ok(res) => res,
    //     Err(e) => return HttpResponse::InternalServerError().body(e.to_string()),
    // };
    // let hoge = serde_json::fo;
    // print!("{}", &res_json);
    // let mut ctx = tera::Context::new();
    // ctx.insert("emo", &res_json);
    // let view = templates.render("hoge.html.tera", &ctx);
    // match view {
    //     Ok(body) => HttpResponse::Ok().content_type("text/html").body(body),
    //     Err(e) => HttpResponse::InternalServerError().body(e.to_string()),
    // }
}

// async fn render_html(json:String, templates: web::Data<Tera>)->Result<String,Error> {
//     let mut ctx = tera::Context::new();
//     ctx.insert("text", "aiueo");
//     templates.render("hoge.html.tera", &ctx)
// }


pub async fn send_post_to_bff(json: serde_json::Value) -> reqwest::Result<String> {
    let client = reqwest::Client::new();
    let responce = client
        .post("http://bff:9000/post")
        .json(&json) //ひどい実装ですみませんが動作確認なので許してほしいです
        .send()
        .await?;
    responce.text().await
}
