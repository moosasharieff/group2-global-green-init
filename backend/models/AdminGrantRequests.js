const mongoose = require('mongoose');


const AdminGrantRequests = new mongoose.Schema({
    id: {
        type:Object,
        required: true,
        alias: '_id'   
    },
    granterName:{
        type:String,
        required: true 
    },
    name: {
        type:String,
        required: true        
    },
    email: {
        type:String,
        required: true        
    },
    grantAmount: {
        type:Number,
        required: true        
    },
    description: {
        type:String,
        required: true       
    },
})

module.exports = mongoose.model('admin-client-grant-request', AdminGrantRequests);