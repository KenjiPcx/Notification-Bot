import express from "express";
import mongoose from "mongoose";
import dotenv from "dotenv";
import eventRouter from "./routes.js";

dotenv.config();

// Config
const port = process.env.PORT || 5000;
const app = express();
app.use(express.urlencoded({ extended: true }));
app.use(express.json());
app.use("/events", eventRouter);

// Connect to DB
mongoose
  .connect(process.env.DB_CONNECTION, {
    useNewUrlParser: true,
    useUnifiedTopology: true,
    useFindAndModify: false,
  })
  .then(() => {
    console.log("Connected");
  })
  .catch((err) => {
    console.log(err);
  });

app.listen(port, (err) => {
  if (err) {
    console.log("Error loading server");
  }
  console.log(`Listening on port http://localhost:${port}`);
});
