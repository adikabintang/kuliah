#include <iostream>
#include <nghttp2/asio_http2_server.h>

using namespace nghttp2::asio_http2;
using namespace nghttp2::asio_http2::server;

int main(int argc, char *argv[])
{
    boost::system::error_code ec;
    boost::asio::ssl::context tls(boost::asio::ssl::context::sslv23);

    tls.use_private_key_file("server.key", boost::asio::ssl::context::pem);
    tls.use_certificate_chain_file("server.pem");

    configure_tls_context_easy(ec, tls);

    http2 server;
    server.num_threads(4);

    // std::string style_css = "h1 { color: green; }";

    // server.handle("/", [&style_css](const request &req, const response &res) {
    //     boost::system::error_code ec;
    //     auto push = res.push(ec, "GET", "/style.css");
    //     push->write_head(200);
    //     push->end(style_css);

    //     res.write_head(200);
    //     res.end(R"(
    //         <!DOCTYPE html><html lang="en">
    //         <title>HTTP/2 FTW</title><body>
    //         <link href="/style.css" rel="stylesheet" type="text/css">
    //         <h1>This should be green</h1>
    //         </body></html>
    //     )");
    // });

    server.handle("/index.html", [](const request &req, const response &res) {
        boost::system::error_code ec;
        auto push = res.push(ec, "GET", "/style.css");
        push->write_head(200);
        push->end(file_generator(("style.css")));

        push = res.push(ec, "GET", "/bootstrap.min.css");
        push->write_head(200);
        push->end(file_generator(("bootstrap.min.css")));
        std::cout << "ec: " << ec.message() << std::endl;

        for (int i = 1; i <= 30; i++) {
            std::string img = "img/" + std::to_string(i) + ".jpeg";
            auto p = res.push(ec, "GET", "/" + img);
            p->write_head(200);
            p->end(file_generator((img)));
            
        }

        res.write_head(200);
        res.end(file_generator("index.html"));
    });

    // server.handle("/style.css",
    //               [&style_css](const request &req, const response &res) {
    //                   res.write_head(200);
    //                   res.end(style_css);
    //               });

    if (server.listen_and_serve(ec, tls, "0.0.0.0", "443"))
    {
        std::cerr << "error: " << ec.message() << std::endl;
    }
}
