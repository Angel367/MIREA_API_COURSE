const express = require('express');
const app = express(); // инициализация объекта приложения
const { graphqlHTTP } = require('express-graphql');
const port = 1234; // номер порта
const schema = require('./schema/schema'); //

app. use(
    "/auto",
    graphqlHTTP({
        schema: schema,
        graphiql: true
    }));
app.listen(port); // прослушиваем порт 1234
