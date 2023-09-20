import jwt from "jsonwebtoken"
export const requireRefreshToken = (req,res,next)=>{
    try {
        const token = req.cookies.refreshToken;
        if(!token)
            throw new Error ("El token does not exist");
        const {uid} = jwt.verify(token,process.env.JWT_REFRESH);
        req.uid=uid;
        next()
    } catch (error) {
        console.log(error);
        return res.status(401).json({error: error.message});
    }
};
