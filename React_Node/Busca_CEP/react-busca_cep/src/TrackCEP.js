import React from "react";
import "./styles/style.css";

function TrackCEP({events}){
    if (!events || events.length === 0 ) return null;    
    
    if (events[0].status !== 200) {
        return(
            <>
                <ul className="list-group">
                    <li className="list-group-item">
                        <span>{events[0].message}</span>
                    </li>
            </ul>
        </>    
        )
    }
    
    return (
        
        <>
            <ul className="list-group">
                {events.map(item => 
                <li className="list-group-item" key={item.status}>
                    <span>CEP: {item.code}</span>
                    <span>Logradouro: {item.address}</span>
                    <span>Bairro: {item.district}</span>
                    <span>Cidade: {item.city}</span>
                    <span>UF: {item.state}</span>
                </li>)}
            </ul>
        </>
    )
}

export default TrackCEP;