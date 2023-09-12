const client = require("./client");
const path = require("path");
const express = require("express");
const bodyParser = require("body-parser");
const app = express();
app.set("views", path.join(__dirname, "."));
app.set("view engine", "hbs");
app.use(bodyParser.json());
app.use(bodyParser.urlencoded({extended: false}));
app.get("/", (req, res) => {
    client.getAll(null, (err, data) => {
        if (!err) {
            res.render("cartobjects", {
                results: data.cartObjects
            });
        }
    });
});
app.post("/save", (req, res) => {
    let newSubscriber = {
        name: req.body.name,
        amount: req.body.amount,
        isBought: req.body.isBought
    };
    client.insert(newSubscriber, (err, data) => {
        if (err) throw err;
        console.log("Продукт создан", data);
        res.redirect("/");
    });
});
app.post("/update", (req, res) => {
    const updateSubscriber = {
        name: req.body.name,
        amount: req.body.amount,
        isBought: req.body.isBought
    };
    client.update(updateSubscriber, (err, data) => {
        if (err) throw err;
        console.log("Продукт успешно обновлён", data);
        res.redirect("/");
    });
});
app.post("/remove", (req, res) => {
    client.remove({name: req.body.name}, (err, _) => {
        if (err) throw err;
        console.log("Продукт удалён");
        res.redirect("/");
    });
});
const PORT = process.env.PORT || 3000;
app.listen(PORT, () => {
    console.log("Сервер запущен на порту %d", PORT);
});