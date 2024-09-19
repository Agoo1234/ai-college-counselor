import React, { useState, useEffect } from 'react';
import axios from 'axios';

const DocumentList = ({ token, onSelectDocument }) => {
    const [documents, setDocuments] = useState([]);

    useEffect(() => {
        const fetchDocuments = async () => {
            try {
                const response = await axios.get('http://localhost:5000/documents', {
                    headers: { Authorization: `Bearer ${token}` }
                });
                setDocuments(response.data);
            } catch (error) {
                console.error('Failed to fetch documents:', error);
            }
        };
        fetchDocuments();
    }, [token]);

    const handleDelete = async (id) => {
        try {
            await axios.delete(`http://localhost:5000/documents/${id}`, {
                headers: { Authorization: `Bearer ${token}` }
            });
            setDocuments(documents.filter(doc => doc.id !== id));
        } catch (error) {
            console.error('Failed to delete document:', error);
        }
    };

    return (
        <div>
            <h2>Documents</h2>
            <ul>
                {documents.map(doc => (
                    <li key={doc.id}>
                        {doc.title}
                        <button onClick={() => onSelectDocument(doc)}>Edit</button>
                        <button onClick={() => handleDelete(doc.id)}>Delete</button>
                    </li>
                ))}
            </ul>
        </div>
    );
};

export default DocumentList;
