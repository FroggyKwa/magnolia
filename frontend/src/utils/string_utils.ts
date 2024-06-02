export default function capitalize(str: string) {
    if (str && str.length)
        return str[0].toUpperCase() + str.slice(1);

}