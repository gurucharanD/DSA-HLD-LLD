import {
    Log,
} from './log';

export const verifyRequestPayload = (req, reqTypeData = 'body') => {
    try {
        const payload = { ...req[reqTypeData] };

        const format = /<[^>]*>/gm;

        for (const key in payload) {
            if (payload[key] &&
                !Array.isArray(payload[key]) &&
                typeof payload[key] !== 'object' &&
                payload[key].toString().match(format)) {
                return {
                    message: `Invalid "${key}" field. Field data "${payload[key]}" is not allowed.`,
                };
            }
        }
        return req;
    } catch (err) {
        Log.child({
            errorMessage: err.message,
            errorStack: err.stack
        }).error('Error in verifyRequestPayload: ');
        return { err };
    }
}
