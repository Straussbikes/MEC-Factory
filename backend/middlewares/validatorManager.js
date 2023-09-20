import { validationResult } from "express-validator";
import {body} from "express-validator";
export const validationResultExpress = (req,res,next)=>{
    const errors = validationResult(req)
    if(!errors.isEmpty()){
        return res.status(400).json({errors:errors.array()});
    }
    next()
};


export const bodyRegisterVal =[
    body('email',"Wrong Format.").trim().isEmail().normalizeEmail(),
    body('password',"Wrong Password: Min 6 characters.").trim().isLength({min:6}),
    body('password',"Wrong Password.").custom((value,{req})=>{
        if(value!=req.body.repassword){
            throw new Error ('Passwords does not match.')
        }
        return value;
    }),
    validationResultExpress,
]

export const bodyLoginVal = [
    body('email',"Wrong Format.").trim().isEmail().normalizeEmail(),
    body('password',"Wrong Password: Min 6 characters.").trim().isLength({min:6}),
    validationResultExpress
]
