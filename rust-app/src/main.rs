use actix_web::web::Data;
use actix_web::{App, HttpServer};
use tera::Tera;
mod server;

#[actix_web::main]
async fn main() -> std::io::Result<()> {
    HttpServer::new(|| {
        let templates = Tera::new("templates/**/*").unwrap();
        App::new()
            .app_data(Data::new(templates))
            .service(server::hello)
            .service(server::post_example)
    })
    .bind(("rust-app", 8080))?
    .run()
    .await
}
