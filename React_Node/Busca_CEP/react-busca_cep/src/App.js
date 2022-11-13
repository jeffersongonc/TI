import React, {useState} from 'react';
import './App.css';
import correiosImage from './assets/correios-logo.png';
import TrackCEP from './TrackCEP';
import InputMask from "react-input-mask";

function App() {
  
  const [events, setEvents] = useState([]);

  const submitHandler = (event) => {
    event.preventDefault();

    const formData = new FormData(event.target);
    const data = Object.fromEntries(formData);
    
    fetch(`http://localhost:3001/tracking/?tracking=${data.tracking}`)
    .then(response => response.json())
    .then(data => {
      let array = [data];
      //console.log(array);
      setEvents(array);
    })
    .catch(error => console.error);
  }
  return (
    <div className="container text-center">
      <h1>Buscar CEP</h1>
      <form onSubmit={submitHandler}>
        <div className="form-group">
          <div className="input-group">
            <InputMask mask='99999999' name="tracking" className="form-control" required></InputMask>
            <span className="input-group-btn">
              <button type="submit" name="TrackCEP" className="btn btn-success">Buscar CEP</button>
            </span>
          </div>          
        </div>        
      </form>
      <div>
        <TrackCEP events={events}/>
      </div>
      <div>
        <img src={correiosImage} alt="" height="200px" />
      </div>      
    </div>
  );
}

export default App;
