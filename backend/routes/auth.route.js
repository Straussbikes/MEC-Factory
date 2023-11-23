import express from "express"
import { pushData,infoUser,login, logout, refreshToken, register,handleResponse, handleEtsi } from "../controllers/auth.controller.js";
import { requireToken } from "../middlewares/requireToken.js";
import { requireRefreshToken } from "../middlewares/requireRefreshToken.js";
import { bodyLoginVal, bodyRegisterVal } from "../middlewares/validatorManager.js";
const router = express.Router()

router.post('/api/v1/login',bodyLoginVal,login);

router.post('/api/v1/register',bodyRegisterVal,register);

router.get('/api/v1/protected',requireToken,infoUser);
router.get('/api/v1/refresh',requireRefreshToken,refreshToken);
router.get('/api/v1/logout',logout)
router.post('/response',handleResponse);
router.get("/api/v1/data",pushData);
router.post("/api/v1/handleEtsi",handleEtsi);
export default  router;