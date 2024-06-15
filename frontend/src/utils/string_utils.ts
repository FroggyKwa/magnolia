export default function capitalize(str: string | undefined) {
    if (str && str.length)
        return str[0].toUpperCase() + str.slice(1);
}