const API_URL = "http://127.0.0.1:8000";

// =============================
// Elements
// =============================

const fileInput = document.getElementById("imageInput");

const uploadBtn = document.getElementById("uploadBtn");

const enhanceBtn = document.getElementById("enhanceBtn");
const denoiseBtn = document.getElementById("denoiseBtn");
const sharpenBtn = document.getElementById("sharpenBtn");
const deblurBtn = document.getElementById("deblurBtn");

const askBtn = document.getElementById("askBtn");

const questionInput = document.getElementById("questionInput");

const originalImage = document.getElementById("originalImage");
const processedImage = document.getElementById("processedImage");

const aiAnswer = document.getElementById("answer");

const statusBox = document.getElementById("status");

const downloadBtn = document.getElementById("downloadBtn");

let uploaded = false;

// Stores the processed image URL
let processedImageURL = "";


// =============================
// Status Helper
// =============================

function setStatus(message, type = "info") {

    statusBox.innerText = message;

    if (type === "success") {

        statusBox.style.background = "#dcfce7";
        statusBox.style.borderLeft = "5px solid #16a34a";
        statusBox.style.color = "#166534";

    }

    else if (type === "error") {

        statusBox.style.background = "#fee2e2";
        statusBox.style.borderLeft = "5px solid #dc2626";
        statusBox.style.color = "#991b1b";

    }

    else {

        statusBox.style.background = "#eaf2ff";
        statusBox.style.borderLeft = "5px solid #2563eb";
        statusBox.style.color = "#1e3a8a";

    }

}


// =============================
// Upload Image
// =============================

uploadBtn.addEventListener("click", async () => {

    if (fileInput.files.length === 0) {

        setStatus("Please choose an image first.", "error");
        return;

    }

    const formData = new FormData();

    formData.append("file", fileInput.files[0]);

    uploadBtn.disabled = true;
    uploadBtn.innerText = "Uploading...";

    setStatus("Uploading image...");

    try {

        const response = await fetch(`${API_URL}/upload`, {
            method: "POST",
            body: formData
        });

        const data = await response.json();

        if (!response.ok) {

            throw new Error(data.detail || "Upload failed.");

        }

        originalImage.src =
            API_URL + data.image_url + "?t=" + Date.now();

        processedImage.src = "";

        processedImageURL = "";

        downloadBtn.style.display = "none";

        aiAnswer.innerHTML = "";

        questionInput.value = "";

        uploaded = true;

        setStatus("Image uploaded successfully.", "success");

    }

    catch (error) {

        console.log(error);

        setStatus(error.message, "error");

    }

    uploadBtn.disabled = false;
    uploadBtn.innerText = "Upload Image";

});


// =============================
// Image Processing
// =============================

async function processImage(endpoint) {

    if (!uploaded) {

        setStatus("Please upload an image first.", "error");
        return;

    }

    setStatus("Processing image...");

    try {

        const response = await fetch(

            `${API_URL}/process/${endpoint}`,

            {
                method: "POST"
            }

        );

        const data = await response.json();

        if (!response.ok) {

            throw new Error(data.detail || "Processing failed.");

        }

        processedImageURL = API_URL + data.image_url;

        processedImage.src =
            processedImageURL + "?t=" + Date.now();

        downloadBtn.style.display = "flex";

        setStatus(
            `Image ${endpoint} completed successfully.`,
            "success"
        );

    }

    catch (error) {

        console.log(error);

        setStatus(error.message, "error");

    }

}


// =============================
// Processing Buttons
// =============================

enhanceBtn.onclick = () => processImage("enhance");

denoiseBtn.onclick = () => processImage("denoise");

sharpenBtn.onclick = () => processImage("sharpen");

deblurBtn.onclick = () => processImage("deblur");


// =============================
// Download Processed Image
// =============================

downloadBtn.addEventListener("click", async () => {

    if (!processedImageURL) {

        setStatus("No processed image available.", "error");
        return;

    }

    try {

        setStatus("Downloading image...");

        const response = await fetch(processedImageURL);

        if (!response.ok) {

            throw new Error("Download failed.");

        }

        const blob = await response.blob();

        const blobURL = window.URL.createObjectURL(blob);

        const a = document.createElement("a");

        a.href = blobURL;

        const filename =
            processedImageURL.split("/").pop();

        a.download = filename;

        document.body.appendChild(a);

        a.click();

        a.remove();

        window.URL.revokeObjectURL(blobURL);

        setStatus("Image downloaded successfully.", "success");

    }

    catch (error) {

        console.log(error);

        setStatus(error.message, "error");

    }

});


// =============================
// Ask AI
// =============================

askBtn.addEventListener("click", async () => {

    if (!uploaded) {

        setStatus("Please upload an image first.", "error");
        return;

    }

    const question = questionInput.value.trim();

    if (question === "") {

        setStatus("Please enter a question.", "error");
        return;

    }

    askBtn.disabled = true;
    askBtn.innerText = "Thinking...";

    aiAnswer.innerHTML = "";

    setStatus("AI is analyzing the image...");

    try {

        const response = await fetch(

            `${API_URL}/inference/ask`,

            {

                method: "POST",

                headers: {

                    "Content-Type": "application/json"

                },

                body: JSON.stringify({

                    question: question

                })

            }

        );

        const data = await response.json();

        console.log("Response:", data);

        if (!response.ok) {

            throw new Error(data.detail || "AI request failed.");

        }

        aiAnswer.innerHTML =
            data.answer || "No response returned.";

        setStatus(
            "AI response generated successfully.",
            "success"
        );

    }

    catch (error) {

        console.log(error);

        aiAnswer.innerHTML = "";

        setStatus(error.message, "error");

    }

    askBtn.disabled = false;
    askBtn.innerText = "Ask AI";

});