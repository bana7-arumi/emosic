use actix_web::web::Data;
use actix_web::{get, post, web, App, HttpResponse, HttpServer, Responder};
use serde::Deserialize;
use tera::Tera;

#[derive(Deserialize)]
struct Example {
    text: String,
}

#[get("/")]
async fn hello(templates: web::Data<Tera>) -> impl Responder {
    let view = templates.render("index.html", &tera::Context::new());

    match view {
        Ok(body) => HttpResponse::Ok().content_type("text/html").body(body),
        Err(e) => HttpResponse::InternalServerError().body(e.to_string()),
    }
}
#[post("/post")]
async fn post_example(item: web::Json<Example>) -> String {
    format!("text: {}\n", item.text)
}
#[actix_web::main]
async fn main() -> std::io::Result<()> {
    HttpServer::new(|| {
        let templates = Tera::new("templates/**/*").unwrap();
        App::new()
            .app_data(Data::new(templates))
            .service(hello)
            .service(post_example)
    })
    .bind(("rust-app", 8080))?
    .run()
    .await
}
