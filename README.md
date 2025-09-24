<b>Distributed Ride Matching Platform</b><br>
<b>Real-time ride-matching service inspired by ride-sharing apps</b><br><br>

<b>Overview</b><br>
This project is a distributed, real-time ride-matching platform designed to simulate the core functionality of popular ride-sharing applications.<br>
It efficiently matches riders with nearby drivers using a microservices architecture, with a React.js frontend for an interactive user interface.<br><br>

<b>Key Features</b><br>
- Real-time rider and driver matching using geospatial data<br>
- Event-driven architecture with Kafka for handling rider and driver events<br>
- Redis for tracking driver locations and availability efficiently<br>
- Feedback storage for rides in a database<br>
- Scalable microservices architecture for easy extensibility<br>
- Interactive frontend built with React.js for riders and drivers<br><br>

<b>Architecture</b><br>
<img width="1536" height="1024" alt="image" src="https://github.com/user-attachments/assets/968f5be3-897c-424f-a1a4-92100f6db778" /><br>
The diagram above shows the microservices setup with Kafka for event streaming, Redis for location tracking, and the interaction between riders and drivers. The React.js frontend interacts with the backend services to send ride requests and display driver locations in real-time.<br><br>

<b>Tech Stack</b><br>
- React.js<br>
- Python / Flask<br>
- Kafka<br>
- Redis<br>
- PostgreSQL / MySQL<br>
- HTML / CSS<br><br>

<b>How It Works</b><br>
- Rider uses the React.js frontend to send a ride request with their location and destination.<br>
- Request is published to a Kafka topic, and driver services consume the event.<br>
- Redis stores current driver locations and availability to find the nearest match.<br>
- Matching driver is assigned to the rider, and both receive notifications via the frontend.<br>
- Ride feedback is collected and stored in the database for future analytics.<br><br>

<b>Future Enhancements</b><br>
- Integration with live maps for automatic location input on the React.js frontend.<br>
- Advanced ride-matching algorithms considering traffic and ETA.<br>
- Mobile app interface for riders and drivers.<br>
- Analytics dashboard for monitoring ride patterns and feedback.<br>
