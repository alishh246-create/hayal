// script.js

// Smooth scroll for navigation links
document.querySelectorAll("nav a").forEach(link => {
  link.addEventListener("click", function (e) {
    e.preventDefault();
    const targetId = this.getAttribute("href");
    const targetSection = document.querySelector(targetId);
    if (targetSection) {
      targetSection.scrollIntoView({ behavior: "smooth" });
    }
  });
});

// Gallery hover alert (demo)
document.querySelectorAll(".gallery img").forEach(img => {
  img.addEventListener("click", () => {
    alert("You clicked on " + img.alt);
  });
});

// WhatsApp button click
const whatsappBtn = document.querySelector(".contact button");
if (whatsappBtn) {
  whatsappBtn.addEventListener("click", () => {
    console.log("WhatsApp button clicked!");
  });
}

// Back to Top button (optional feature)
const backToTop = document.createElement("button");
backToTop.innerText = "⬆ Top";
backToTop.style.position = "fixed";
backToTop.style.bottom = "20px";
backToTop.style.right = "20px";
backToTop.style.padding = "10px 15px";
backToTop.style.background = "#fafafaff";
backToTop.style.color = "#0c0101ff";
backToTop.style.border = "none";
backToTop.style.borderRadius = "8px";
backToTop.style.cursor = "pointer";
backToTop.style.display = "none";

document.body.appendChild(backToTop);

window.addEventListener("scroll", () => {
  if (window.scrollY > 200) {
    backToTop.style.display = "block";
  } else {
    backToTop.style.display = "none";
  }
});

backToTop.addEventListener("click", () => {
  window.scrollTo({ top: 0, behavior: "smooth" });
});

function DARKMODE() {
  document.body.classList.toggle('dark-mode');
}
let topBtn = document.getElementById("topBtn");
window.onscroll = function() {
  if (document.body.scrollTop > 200 || document.documentElement.scrollTop > 200) {
    topBtn.style.display = "block";
  } else {
    topBtn.style.display = "none";
  }
};
topBtn.onclick = function() {
  window.scrollTo({top: 0, behavior: 'smooth'});
};
function openLightbox(img) {
  document.getElementById('lightbox').style.display = 'flex';
  document.getElementById('lightbox-img').src = img.src;
}
document.getElementById('contactForm').addEventListener('submit', function(e) {
  e.preventDefault();

  const name = document.getElementById('name').value.trim();
  const email = document.getElementById('email').value.trim();
  const phone = document.getElementById('phone').value.trim();
  const eventType = document.getElementById('eventType').value;
  const message = document.getElementById('message').value.trim();
  const successMsg = document.getElementById('successMsg');

  if (name && email && phone && eventType && message) {
    successMsg.textContent = "✅ Thank you, " + name + "! Your event request has been sent successfully.";
    this.reset();
  } else {
    successMsg.textContent = "❌ Please fill all fields before submitting.";
  }
});
