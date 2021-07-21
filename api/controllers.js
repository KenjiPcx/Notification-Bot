import Event from "./models.js"

export const createEvent = async (req, res) => {
    try {
        const event = Event({
          name: req.body.name,
          day: req.body.day,
          month: req.body.month,
          organizer: req.body.organizer,
          category: req.body.category,
        });

        await event.save()
        res.status(200).json(event)
    } catch (err) {
        res.status(400).json({err: "Failed to Create Event"})
    }
}

export const getAllEvents = async (req, res) => {
    try {
        const events = await Event.find()
        
        res.status(200).json(events)
    } catch (err) {
        res.status(400).json({ err: "Failed to Get Events" })
    }
}
