function generateAPIKey() {
    let r = Math.random().toString(36).substr(2, 10);
    api_token_input = document.getElementById("api-key");

    api_token_input.value = r;
}