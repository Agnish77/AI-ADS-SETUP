import React, { useState } from "react";
import axios from "./api";

const AdPreview = ({ adData }) => {
    const submitAd = async () => {
        const res = await axios.post("/create-ad", adData);
        console.log("Ad Created:", res.data);
    };

    return (
        <div>
            <h2>Ad Preview</h2>
            <p><strong>Title:</strong> {adData.title}</p>
            <p><strong>Description:</strong> {adData.description}</p>
            <button onClick={submitAd}>Launch Ad</button>
        </div>
    );
};

export default AdPreview;
