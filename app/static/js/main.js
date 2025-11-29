// Login form Loading Spinner button
document.addEventListener('DOMContentLoaded', function () {
    const loginForm = document.querySelector('form[data-login-form]');
    if (!loginForm) return; // If not on login page, exit safely

    const submitButton = loginForm.querySelector('[data-login-submit]');
    if (!submitButton) return;

    loginForm.addEventListener('submit', function () {
        // If already in loading state, prevent double-trigger
        if (submitButton.classList.contains('is-loading')) {
            return;
        }

        submitButton.classList.add('is-loading');
        submitButton.disabled = true; // Prevent double submit
    });
});