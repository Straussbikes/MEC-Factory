import "dotenv/config";
import "./database/connectdb.js";
import  express  from "express";
import cors from "cors";
import authRouter from './routes/auth.route.js';
import cookieParser from "cookie-parser";

const app = express();
const whiteList=[process.env.ORIGIN1];



app.use(cors({
    origin: function(origin,callback){
        if(!origin ||whiteList.includes(origin)){
            return callback(null,origin);
        }
        return callback(
            "Error cors origin "  + origin
        );
    },
    credentials: true,
}))

app.use(cookieParser());
app.use(express.json());
app.use('',authRouter);



const  PORT = process.env.PORT || 5000
app.listen(PORT,()=> console.log("http://localhost:" + PORT));