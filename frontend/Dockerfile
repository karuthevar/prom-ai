# frontend/Dockerfile

FROM node:20-alpine

WORKDIR /app

# Copy package.json and install dependencies
COPY package*.json ./
RUN npm install

# Install Tailwind and init config
RUN npm install -D tailwindcss postcss autoprefixer && \
    npx tailwindcss init -p

# Copy rest of the application
COPY . .

# Build the frontend using Vite
RUN npm run build

# Start app using dev server (for demo)
EXPOSE 5173
CMD ["npm", "run", "dev"]
