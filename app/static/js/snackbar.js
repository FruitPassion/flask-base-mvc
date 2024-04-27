function myFunction(message, color) {
    if (!['success', 'danger', 'warning', 'info'].includes(color)) {
        color = 'info';
    }
    let snack = document.getElementById("snackbar");

    snack.innerHTML = message;
    // add to classlist
    snack.classList.add('show');
    snack.classList.add("bg-" + color);
    setTimeout(function() {
        snack.classList.remove('show');
        snack.classList.remove("bg-" + color);
    }, 3000);
}