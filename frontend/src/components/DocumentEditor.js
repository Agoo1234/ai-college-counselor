import React, { useState, useEffect } from 'react';
import axios from 'axios';

const DocumentEditor = ({ token, document, onSave }) => {
    const [title, setTitle] = useState('');
    const [content, setContent] = useState('');

    useEffect(() => {
        if (document) {
            setTitle(document.title);
            setContent(document.content);
        }
    }, [document]);

    const handleSubmit = async (e) => {
        e.preventDefault();
        try {
            if (document) {
                await axios.put(`http://localho.st:5000/documents/${document.id}`,
                    { title, content },
                    { headers: { Authorization: `Bearer ${token}` } }
                );
            } else {
                await axios.post('http://localho.st:5000/documents',
                    { title, content },
                    { headers: { Authorization: `Bearer ${token}` } }
                );
            }
            onSave();
        } catch (error) {
            console.error('Failed to save document:', error);
        }
    };

    return (
        <form onSubmit={handleSubmit}>
            <input type="text" value={title} onChange={(e) => setTitle(e.target.value)} placeholder="Title" required />
            <textarea value={content} onChange={(e) => setContent(e.target.value)} placeholder="Content" required />
            <button type="submit">Save</button>
        </form>
    );
};

export default DocumentEditor;
