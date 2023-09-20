
import mongoose from "mongoose";

try{
   await mongoose.connect(process.env.URI_MONGO)
   console.log("Connected to DB ok 👌 ")
}catch (error){
   console.log("Conection error : "+ error)
}

