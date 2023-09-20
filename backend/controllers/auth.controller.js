import { Pedido, User } from "../models/user.js";
import jwt from "jsonwebtoken";
import {generateRefreshToken, generateToken} from "../utils/tokenManager.js";


export const login =async (req,res)=>{
    console.log("login");
   try {
    const {name,email,password}=req.body;
    let users = await User.findOne({email});
    if(!users) return res.status(403).json({error: "User does not exists."});
    const isEqual = await users.comparePassword(password);
    if(!isEqual){
        return res.status(403).json({error:"Wrong Password."})
    }
    //generate token
    const {token,expiresIn}= generateToken(users.id)
    generateRefreshToken(users.id,res);

    return res.json({ok:token,expiresIn});
   } catch (error) {
    console.log(error);
    return res.status(500).json({error: "Server error"}); 
   }
    res.json({ok:"Login"});
};

export const register =async (req,res)=> {
   console.log("registo")
    const {name,email,password} = req.body;
    
    try {
        
        const user = new User({name,email,password});
        let users = await User.findOne({email});
        if(users) throw {code:11000};
         
        await user.save();
        return res.json({ok:true});
    } catch (error) {
        console.log(error)
        if(error.code==11000) return res.status(400).json({error: "User already exists."}); 
    }
};

export const infoUser= async(req,res)=>{
    try {
        const user = await User.findById(req.uid).lean()
        return res.json({uid:user.uid,name:user.name,email:user.email})
    } catch (error) {
        return res.status(500).json({error:"Server error"})
    }
   

};

export const refreshToken = (req,res)=> {
    try {
     
        const {token,expiresIn} = generateToken(req.uid);
        return res.json({token,expiresIn});
    } catch (error) {
        console.log(error)
        return res.status(500).json({error:"server error"})
    }
   
    
};
export const logout = async  (req,res) => {

    const email=req.query.email
    try {
        res.clearCookie('refreshToken');
        res.json({ok:true})
        const resp = await Pedido.deleteMany({email:email});
    } catch (error) {
        console.log(error)
    }
};

export const handleResponse = async (req,res) =>{
    try {
        
        const {appId,request,response,flag,erro,date,solution,newUrl,email} = req.body;
      
        
        const pedidoss = new Pedido({appId,request,response,erro,date,solution,newUrl,email});
        console.log(email)
        await pedidoss.save();
        res.json({ message: 'Data received successfully' });
      
    } catch (error) {
      console.error("error from httpServer : "+error);  
    }
};

export const pushData = async(req,res) =>{
    try {
        const  email=req.query.email
        let pedido=await Pedido.findOneAndDelete({email:email}).sort()
        if(pedido==undefined)
        {
            res.json(null)
        }else{
            res.json(pedido)
            
        }
      
        
    } catch (error) {
        console.error(error);
    }

}