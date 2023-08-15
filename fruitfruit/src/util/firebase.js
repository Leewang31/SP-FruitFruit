import firebase from "firebase/app";
import "firebase/firestore";

// Your web app's Firebase configuration
const firebaseConfig = {
    apiKey: "AIzaSyAzX-t3FXKYLzX7E9IZay6cVBRVj5Ioe9k",
    authDomain: "watermelon-9b7b5.firebaseapp.com",
    projectId: "watermelon-9b7b5",
    storageBucket: "watermelon-9b7b5.appspot.com",
    messagingSenderId: "1023119934106",
    appId: "1:1023119934106:web:ab6cc28904f2dbabd5d523"
};

if (!firebase.apps.length) {
    firebase.initializeApp(firebaseConfig);
}

const db = firebase.firestore();
export { db };