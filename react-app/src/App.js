import React from 'react';
import {Routes, Route} from 'react-router-dom'
import NotFound from './pages/NotFound/NotFound';
import Company from './pages/Company/Company';

function App() {
  return (
    <div className="App">
      <Routes>
         <Route path="/:slug" element={<Company/>}  />
         <Route path="*"  element={ <NotFound/>} />
      </Routes>
    </div>
  )
}

export default App