import jwt from "jsonwebtoken"
export const requireToken = (req,res,next)=>{
    try {
        const token = req.headers?.authorization;
        if(!token)
            throw new Error ("El token does not exist use Bearer");
        const tokens= token.split(" ")[1];
        const {uid} = jwt.verify(tokens,process.env.JWT_SECRET);
        req.uid=uid;
        next()
    } catch (error) {
        console.log(error);
        return res.status(401).json({error: error.message});
    }
};
