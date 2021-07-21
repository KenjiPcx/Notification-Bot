import mongoose from "mongoose";

const eventSchema = mongoose.Schema({
  name: { type: String, required: true },
  day: Number,
  month: Number,
  organizer: String,
  category: String,
});

const Event = mongoose.model("Event", eventSchema)

export default Event;
