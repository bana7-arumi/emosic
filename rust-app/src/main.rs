use actix_web::{get, post, web, App, HttpResponse, HttpServer, Responder};

async fn home() -> impl Responder {
    HttpResponse::Ok().body("Hello")
}

#[actix_web::main]
async fn main() -> std::io::Result<()> {
    HttpServer::new(|| { 
        App::new()
            .route("/", web::get().to(home))
    })
    .bind(("127.0.0.1", 8080))?
    .run()
    .await
}
