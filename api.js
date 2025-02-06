import React, { useState } from "react";
import Chatbot from "./Chatbot";
import AdPreview from "./AdPreview";

function App() {
    const [adData, setAdData] = useState(null);

    return (
        <div>
            <Chatbot setAdData={setAdData} />
            {adData && <AdPreview adData={adData} />}
        </div>
    );
}

export default App;
