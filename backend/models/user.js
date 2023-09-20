import mongoose, { mongo } from "mongoose";
import bcryptjs from "bcryptjs";
const {Schema,model }=mongoose;
const pedidoss = new mongoose.Schema({
    appId:{
        type:String,
        required:true,
        unique:true,
        index:{unique:true}
    },
    request:{
        type:String,
        required:true
    },
    response:{
        type:String,
        required:true
    },
    erro:{
        type:String,
        required:true
    },
    date:{
        type:String,
        required:true
    },
    solution:{
        type:String,
        required:true
    },
    newUrl:{
        type:String,
        
    },
  
});
const userSchema= new mongoose.Schema({
    name:{
        type:String,
        required : true

    },
    email:{
        type:String,
        required:true,
        unique:true,
        index:{unique:true}
    },
    password:{
        type:String,
        required:true
    },
    pedidos:[pedidoss],
});
userSchema.pre("save",async function(next){
    const user = this
    if(!user.isModified('password')) return next()
    try {
        const salta = await bcryptjs.genSalt(10);
        user.password=await bcryptjs.hash(user.password,salta);
        next();
    } catch (error) {
        console.log(error)
        throw new Error("Problems coding to hash");
    }
})
userSchema.methods.comparePassword = async function (frontendPassword){
    return await bcryptjs.compare(frontendPassword,this.password);
}

export const User = mongoose.model('User',userSchema)
export const Pedido = mongoose.model("Pedido",pedidoss)

