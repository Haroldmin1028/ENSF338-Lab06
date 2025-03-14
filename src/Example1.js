import React from 'react';
import { useState, useEffect } from 'react';

function Example1() {
    const [count, setCount] = useState(0);
    
    useEffect(() => { // Effect for running code on the initial render
        console.log('Run on the initial render.'); 
    }, []);
    
    useEffect(() => {// Effect for running code on the first render when the 'count' state changes
        console.log('Count has changed:', count); 
    }, [count]);
    
    return (
        <div>
            <p>Count: {count}</p>
            <button onClick={() => setCount(count + 1)}>Increment</button>
        </div>
    );
};

export default Example1;
