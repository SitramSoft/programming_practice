# Practice JavaScript programming language

## Instalation

### Ubuntu

- Node.js binary distributions are available from [NodeSource](https://github.com/nodesource/distributions).

- Download and import the Nodesource GPG key

```bash
sudo apt-get update
sudo apt-get install -y ca-certificates curl gnupg
sudo mkdir -p /etc/apt/keyrings
curl -fsSL https://deb.nodesource.com/gpgkey/nodesource-repo.gpg.key | sudo gpg --dearmor -o /etc/apt/keyrings/nodesource.gpg
```

- Create deb repository

```bash
NODE_MAJOR=20
echo "deb [signed-by=/etc/apt/keyrings/nodesource.gpg] https://deb.nodesource.com/node_$NODE_MAJOR.x nodistro main" | sudo tee /etc/apt/sources.list.d/nodesource.list
```

- Run Update and install

```bash
sudo apt-get update
sudo apt-get install nodejs -y
```

- Unsinstalling Node.js

```bash
apt-get purge nodejs &&\
rm -r /etc/apt/sources.list.d/nodesource.list &&\
rm -r /etc/apt/keyrings/nodesource.gpg
```

- Test installed node.js version by checking the output of the following command

```bash
node -v
```

### ArchLinux

```bash
pacman -S nodejs npm
```

- Test installed node.js version by checking the output of the following command

```bash
node -v
```

## 11.12.2023


## 10.12.2023

- Introduction to JavaScript Programming language synthax can be from freeCodeCamp - [Learn JavaScript for beginners](https://www.freecodecamp.org/news/learn-javascript-for-beginners/)

- [Chapter 12](https://www.freecodecamp.org/news/learn-javascript-for-beginners/#12controlflowsloopsinjavascript)
