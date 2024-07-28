



const firebaseConfig = {
  apiKey: "AIzaSyD0oyq0DTUwTC33dOxKxfULyP8rZjmwHC0",
  authDomain: "codemate-26860.firebaseapp.com",
  databaseURL: "https://codemate-26860-default-rtdb.firebaseio.com",
  projectId: "codemate-26860",
  storageBucket: "codemate-26860.appspot.com",
  messagingSenderId: "655654957021",
  appId: "1:655654957021:web:19ea5a602d11dcdff71034",
  measurementId: "G-GRJFG08YD9"
};


// initialize firebase
firebase.initializeApp(firebaseConfig);

// reference your database
var contactFormDB = firebase.database().ref("contactForm");

document.getElementById("contactForm").addEventListener("submit", submitForm);

function submitForm(e) {
e.preventDefault();

var name = getElementVal("name");
var email = getElementVal("email");
var message = getElementVal("message");

saveMessages(name, email, message);
alert('Thank you for your message! We will get back to you soon.');
this.reset();


 }

const saveMessages = (name, email, message) => {
var newcontactForm = contactFormDB.push();

  newcontactForm.set({
     name: name,
     email: email,
     message: message,
  });
 };

const getElementVal = (id) => {
return document.getElementById(id).value;
};


 