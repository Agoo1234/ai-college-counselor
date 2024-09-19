import React, { useState, useEffect } from 'react';
import axios from 'axios';

const Profile = ({ token }) => {
    const [profile, setProfile] = useState(null);
    const [name, setName] = useState('');
    const [dreamCollege, setDreamCollege] = useState('');

    useEffect(() => {
        const fetchProfile = async () => {
            try {
                const response = await axios.get('http://localhost:5000/profile', {
                    headers: { Authorization: `Bearer ${token}` }
                });
                setProfile(response.data);
                setName(response.data.name);
                setDreamCollege(response.data.dream_college);
            } catch (error) {
                console.error('Failed to fetch profile:', error);
            }
        };
        fetchProfile();
    }, [token]);

    const handleSubmit = async (e) => {
        e.preventDefault();
        try {
            await axios.put('http://localhost:5000/profile', 
                { name, dream_college: dreamCollege },
                { headers: { Authorization: `Bearer ${token}` } }
            );
            alert('Profile updated successfully!');
        } catch (error) {
            console.error('Failed to update profile:', error);
        }
    };

    if (!profile) return <div>Loading...</div>;

    return (
        <div>
            <h2>Profile</h2>
            <form onSubmit={handleSubmit}>
                <input type="text" value={name} onChange={(e) => setName(e.target.value)} placeholder="Name" />
                <input type="text" value={dreamCollege} onChange={(e) => setDreamCollege(e.target.value)} placeholder="Dream College" />
                <button type="submit">Update Profile</button>
            </form>
        </div>
    );
};

export default Profile;
