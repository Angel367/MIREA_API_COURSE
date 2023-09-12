const PROTO_PATH = "./cart.proto"


const grpc = require("grpc");
const protoLoader = require("@grpc/proto-loader");

var packageDefinition = protoLoader.loadSync(PROTO_PATH, {
    keepCase: true,
    longs: String,
    enums: String,
    arrays: true
});

const phonebookProto = grpc.loadPackageDefinition(packageDefinition);

const SubscriberService = phonebookProto.phonebook.CartService;
const client = new SubscriberService(
    "localhost:50051",
    grpc.credentials.createInsecure()
);

module.exports = client;