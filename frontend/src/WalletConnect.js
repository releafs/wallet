import React, { useState } from 'react';
import { Web3Provider } from '@ethersproject/providers';

const WalletConnect = ({ args, sendMessage }) => {
    const [walletAddress, setWalletAddress] = useState('');

    const connectWallet = async () => {
        if (window.ethereum) {
            try {
                const provider = new Web3Provider(window.ethereum);
                await provider.send('eth_requestAccounts', []);
                const signer = provider.getSigner();
                const address = await signer.getAddress();
                setWalletAddress(address);
                sendMessage(address); // Send the wallet address back to Streamlit
            } catch (error) {
                console.error('Error connecting wallet:', error);
            }
        } else {
            alert('Please install MetaMask!');
        }
    };

    return (
        <div>
            <button onClick={connectWallet}>Connect Wallet</button>
            {walletAddress && <p>Connected: {walletAddress}</p>}
        </div>
    );
};

export default WalletConnect;
