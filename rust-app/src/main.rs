use actix_web::{get, web, App, HttpResponse, HttpServer, Responder};
use actix_web::web::Data;
use tera::Tera;
#[get("/")]
async fn hello(templates: web::Data<Tera>) -> impl Responder {
    let view = templates.render("index.html", &tera::Context::new());

    match view {
        Ok(body) => HttpResponse::Ok().content_type("text/html").body(body),
        Err(e) => HttpResponse::InternalServerError().body(e.to_string()),
    }
}

async fn manual_hello() -> impl Responder {
    HttpResponse::Ok().body("Hey there!!")
}

#[actix_web::main]
async fn main() -> std::io::Result<()> {
    HttpServer::new(|| {
        let templates = Tera::new("templates/**/*").unwrap();
        App::new()
            .app_data(Data::new(templates))
            .service(hello)
            .route("/hey", web::get().to(manual_hello))
    })
    .bind(("rust-app", 8080))?
    .run()
    .await
}
