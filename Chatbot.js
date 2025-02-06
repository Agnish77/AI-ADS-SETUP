import React, { useState } from "react";
import axios from "./api";

const Chatbot = () => {
    const [messages, setMessages] = useState([]);
    const [input, setInput] = useState("");

    const sendMessage = async () => {
        if (!input) return;
        setMessages([...messages, { text: input, sender: "user" }]);

        const res = await axios.post("/chatbot", { user_input: input });
        setMessages([...messages, { text: res.data.response, sender: "bot" }]);
        setInput("");
    };

    return (
        <div>
            <div>
                {messages.map((msg, i) => (
                    <p key={i} className={msg.sender}>{msg.text}</p>
                ))}
            </div>
            <input value={input} onChange={(e) => setInput(e.target.value)} />
            <button onClick={sendMessage}>Send</button>
        </div>
    );
};

export default Chatbot;
