import express from "express";
import { createEvent, getAllEvents } from "./controllers.js";

const eventRouter = express.Router();

eventRouter.get("/", getAllEvents);

eventRouter.post("/", createEvent);

export default eventRouter;