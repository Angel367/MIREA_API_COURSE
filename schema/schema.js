const graphql = require('graphql');
const {
    GraphQLObjectType,
    GraphQLSchema,
    GraphQLNonNull,
    GraphQLID,
    GraphQLString,
    GraphQLInt,
    GraphQLList
} = graphql;
const cars = [
    { id: 1, title: 'W211 2002', price: 450000, age: 21, brand: 'mercedes' },
    { id: 2, title: 'M5', price: 22500000, age: 3, brand: 'bmw' },
    { id: 3, title: 'quadro', price: 4500000, age: 8 }
];

const CarType = new GraphQLObjectType({
    name: 'CarType',
    fields: () => ({
        id: { type: new GraphQLNonNull(GraphQLID) },
        title: { type: new GraphQLNonNull(GraphQLString) },
        price: { type: new GraphQLNonNull(GraphQLInt) },
        age: { type: new GraphQLNonNull(GraphQLInt) },
        brand: { type: GraphQLString }
    })
})

const RootQueryType = new GraphQLObjectType({
    name: 'RootQueryType',
    fields: () => ({
        info: {
            type: GraphQLString,
            resolve: (parent, args) => 'Hello World!'
        },
        car: {
            type: CarType,
            args: {
                id: { type: GraphQLID }
            },
            resolve: (parent, args) => cars.find(car => car.id === args.id)
        },
        cars: {
            type: new GraphQLList(CarType),
            resolve: () => cars
        }
    })
});
const Mutations = new GraphQLObjectType({
    name: 'Mutations',
    fields: () => ({
        addCar: {
            type: CarType,
            args: {
                id: { type: new GraphQLNonNull(GraphQLID) },
                title: { type: new GraphQLNonNull(GraphQLString) },
                price: { type: new GraphQLNonNull(GraphQLInt) },
                age: { type: new GraphQLNonNull(GraphQLInt) },
                brand: { type: GraphQLString }
            },
            resolve: (parent, args) => {
                const arrLength = cars.push(args)
                return cars[arrLength - 1]
            }
        }
    })
})
module.exports = new GraphQLSchema({
    query: RootQueryType,
    mutation: Mutations,
});
