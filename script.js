document.getElementById('download-resume').addEventListener('click', function() {
    window.open('path/to/your/resume.pdf', '_blank');
});

document.getElementById('contact-form').addEventListener('submit', function(event) {
    event.preventDefault();
    
    const name = document.getElementById('name').value;
    const email = document.getElementById('email').value;
    const message = document.getElementById('message').value;
    
    // Simulate form submission (e.g., send data to an email service or server)
    alert(`Thank you, ${name}! Your message has been sent.`);
    
    // Reset form fields
    document.getElementById('contact-form').reset();
});
