const PROTO_PATH = "./cart.proto";
var grpc = require("grpc");
var protoLoader = require("@grpc/proto-loader");
var packageDefinition = protoLoader.loadSync(PROTO_PATH, {
    keepCase: true,
    longs: String,
    enums: String,
    arrays: true
});
var phonebookProto = grpc.loadPackageDefinition(packageDefinition);
const SubscriberService = phonebookProto.phonebook.CartService;
const {v4: uuidv4} = require("uuid");
const server = new grpc.Server();
// ... (предыдущий код)

const cartObjects = [
    {
        name: "Молоко",
        amount: 3,
        isBought: false
    },
    {
        name: "Хлеб",
        amount: 7,
        isBought: true
    }
];

server.addService(phonebookProto.phonebook.CartService.service, {
    getAll: (_, callback) => {
        callback(null, { cartObjects });
        console.log(cartObjects)
    },
    get: (call, callback) => {
        let cartObject = cartObjects.find(obj => obj.name === call.request.name);
        if (cartObject) {
            callback(null, cartObject);
        } else {
            callback({
                code: grpc.status.NOT_FOUND,
                details: "Не найдено"
            });
        }
    },
    insert: (call, callback) => {
        let cartObject = call.request;
        cartObjects.push(cartObject);
        callback(null, cartObject);
    },
    update: (call, callback) => {
        let existingCartObject = cartObjects.find(obj => obj.name === call.request.name.slice(str.indexOf(',') + 1));
        console.log(call.request.name[1])
        if (existingCartObject) {
            existingCartObject.amount = call.request.amount;
            existingCartObject.isBought = call.request.isBought;
            callback(null, existingCartObject);
        } else {
            callback({
                code: grpc.status.NOT_FOUND,
                details: "Не найдено"
            });
        }
    },
    remove: (call, callback) => {
        let existingCartObjectIndex = cartObjects.findIndex(obj => obj.name === call.request.name);
        if (existingCartObjectIndex !== -1) {
            cartObjects.splice(existingCartObjectIndex, 1);
            callback(null, {});
        } else {
            callback({
                code: grpc.status.NOT_FOUND,
                details: "Не найдено"
            });
        }
    }
});

// ... (остальной код)
server.bind("127.0.0.1:50051", grpc.ServerCredentials.createInsecure());
console.log("Сервер запущен по адресу http://127.0.0.1:50051");
server.start();