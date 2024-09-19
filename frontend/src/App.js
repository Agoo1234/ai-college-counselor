import React, { useState } from 'react';
import Login from './components/Login';
import Register from './components/Register';
import Profile from './components/Profile';
import DocumentList from './components/DocumentList';
import DocumentEditor from './components/DocumentEditor';

function App() {
  const [token, setToken] = useState(null);
  const [selectedDocument, setSelectedDocument] = useState(null);

  if (!token) {
    return (
      <div>
        <h1>Document Management System</h1>
        <Login setToken={setToken} />
        <Register />
      </div>
    );
  }

  return (
    <div>
      <h1>Document Management System</h1>
      <Profile token={token} />
      <DocumentList token={token} onSelectDocument={setSelectedDocument} />
      <DocumentEditor token={token} document={selectedDocument} onSave={() => setSelectedDocument(null)} />
    </div>
  );
}

export default App;
