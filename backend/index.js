import "dotenv/config";
import "./database/connectdb.js";
import  express  from "express";
import cors from "cors";
import authRouter from './routes/auth.route.js';
import cookieParser from "cookie-parser";

const app = express();
const whiteList=[process.env.ORIGIN1," https://frontend-dxox.onrender.com",
                44.226.145.213,
                54.187.200.255,
                34.213.214.55,
                35.164.95.156,
                44.230.95.183,
                44.229.200.200
                ];


app.use(cors({
    origin: function(origin, callback) {
        console.log(req.headers); 
        if (!origin || whiteList.includes(origin)) {
            console.log(origin);
            return callback(null, origin);
        }
        return callback(
            new Error("Error cors origin " + origin)
        );
    },
    credentials: true,
}));
app.use(cookieParser());
app.use(express.json());
app.use('',authRouter);



const  PORT = process.env.PORT || 5000
app.listen(PORT,()=> console.log("http://localhost:" + PORT));
