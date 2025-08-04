// Wait for the HTML content to fully load before running the script
document.addEventListener('DOMContentLoaded', () => {

    // Get references to our interactive HTML elements
    const generateBtn = document.getElementById('generate-btn');
    const copyBtn = document.getElementById('copy-btn');
    const patientMessageTextarea = document.getElementById('patient-message');
    const aiResponseTextarea = document.getElementById('ai-response');

    // --- Generate Button Functionality ---
    generateBtn.addEventListener('click', async () => {
        const patientMessage = patientMessageTextarea.value.trim();

        if (!patientMessage) {
            alert('Please enter a patient message.');
            return;
        }

        // Give user visual feedback while waiting for the AI
        generateBtn.disabled = true;
        generateBtn.textContent = 'Generating...';
        aiResponseTextarea.value = 'Thinking...'; // Placeholder text

        try {
            // Send the patient's message to our backend API
            const response = await fetch('/api/generate-response', {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({ patient_message: patientMessage }),
            });

            const data = await response.json();

            if (!response.ok) {
                // If the server returned an error, display it
                throw new Error(data.error || 'An unknown server error occurred.');
            }

            // Display the AI's response
            aiResponseTextarea.value = data.ai_response;

        } catch (error) {
            console.error('Error:', error);
            aiResponseTextarea.value = `Error: ${error.message}`;
        } finally {
            // Restore the button to its original state
            generateBtn.disabled = false;
            generateBtn.textContent = 'Generate Response';
        }
    });

    // --- Copy Button Functionality ---
    copyBtn.addEventListener('click', () => {
        if (aiResponseTextarea.value) {
            navigator.clipboard.writeText(aiResponseTextarea.value).then(() => {
                // Let the user know the copy was successful
                copyBtn.textContent = 'Copied!';
                setTimeout(() => { copyBtn.textContent = 'Copy Text'; }, 2000);
            });
        }
    });
});